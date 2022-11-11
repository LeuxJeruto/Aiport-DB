from django.test import Client, TestCase

from .models import Airport, Flight, Passanger 

# Create your tests here.
#These are dummy flights and airports in a separate db used for testing our actual code in DB

class FlightTestCase(TestCase):

    def setUp(self):

        #create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        #create flights.
        Flights.objects.create(origin=a1, destination=a2, duration=100)
        Flights.objects.create(origin=a1, destination=a1, duration=200)
        Flights.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.depatures.count(), 3)
    
    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Aiport.objects.gt(code="BBB")
        f = flights.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())
        
    def test_invalid_flight_destinaton(self):
        a1 = Aiport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = Aiport.objects.get(code="AAA")
        a2 = Aiport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())
      

    
