

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'brian_charts.html')


class ChartData(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        
        weeks = []
        sales_19 = []

        qs = Sales2_Sales_Measures_by_Period.values('wm_week').filter(wm_week_contains = '2019').annotate(Sum('pos_sales'))
        for i in qs:
            weeks.append(i['pos_sales__sum'])
            sales_19.append(i['wm_week'])
        data = {
            "weeks": weeks,
            "sales_19": sales_19,
            
        }
        return Response(data) 