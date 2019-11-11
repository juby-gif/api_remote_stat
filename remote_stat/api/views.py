from rest_framework import status, response, views
from foundation.models import StatisticsMemory
import statistics

class AddAPIView(views.APIView):
    def post(self, request):
        unsanitized_stat_value = request.data.get('number',None)

        if unsanitized_stat_value == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                  'message': 'Missing number field.',
                  })
        else:
            try:
                sanitized_stat_value = float(unsanitized_stat_value)
            except Exception as e:
                return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                     'message': 'The number you submitted is not a number.',
                     }
                     )
        memory =  StatisticsMemory.objects.create(value = sanitized_stat_value)
        memory.save()
        return response.Response(
        status=status.HTTP_200_OK,
        data={
             'message': 'The number you entered, '+ str(unsanitized_stat_value)+', was saved successfully!' ,
             }
             )

class AverageAPIView(views.APIView):
    def get(self,request):
        sum = 0
        data = StatisticsMemory.objects.all().order_by('id').values('value')
        length_of_memory_elements = len(data)
        for datum in data:
            sum = sum + datum['value']
        average = sum/length_of_memory_elements
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Average': 'The average is ' + str(average),
            }
        )

class MeanAPIView(views.APIView):
    def get(self,request):
        sum = 0
        data = StatisticsMemory.objects.all().order_by('id').values('value')
        length_of_memory_elements = len(data)
        for datum in data:
            sum = sum + datum['value']
        mean = sum/length_of_memory_elements
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Mean': 'The mean is ' + str(mean),
            }
        )


class StatisticsAPIView(views.APIView):
    def get(self,request):
        data = StatisticsMemory.objects.all().order_by('id').values('value')
        print(data)
        length_of_memory_elements = len(data)
        memory_data_list=[]
        for datum in data:
            memory_data_list.append(datum['value'])
        print(memory_data_list)
        mean = statistics.mean(memory_data_list)
        mode = statistics.mode(memory_data_list)
        median = statistics.median(memory_data_list)
        standard_deviation = statistics.stdev(memory_data_list)
        variance = statistics.variance(memory_data_list)
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'mean': 'The mean is ' + str(mean),
                'mode': 'The mode is ' + str(mode),
                'median': 'The median is ' + str(median),
                'standard_deviation': 'The standard_deviation is ' + str(standard_deviation),
                'variance': 'The variance is ' + str(variance),
            }
        )

class ClearAPIView(views.APIView):
    def post(self,request):
        memory =  StatisticsMemory.objects.all()
        memory.delete()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': "Memory has been cleared successfully!",
            }
        )
