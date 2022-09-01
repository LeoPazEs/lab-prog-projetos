from django.test import TestCase
from django.test import Client 
from django.urls import reverse
from .views import CARS

class CarViewsTestCase(TestCase): 
    client = Client()

    
    def test_list_car_view(self): 
        response = CarViewsTestCase.client.get(reverse("list_carros"))    
        self.assertEquals(response.context["obj_list"], CARS)  

    def test_detalhe_car_view(self): 
        response = CarViewsTestCase.client.get(reverse("detalhe_carro", kwargs={"id" : 1}))  
        print(response.context["obj"])  
        self.assertEquals(response.context["obj"], CARS[1])  





