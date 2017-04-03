import grpc
import random
import customer_pb2
import customer_pb2_grpc


def create_customer(stub):
	print ("-----------Creating Customer-----------")

	try:
		customer = customer_pb2.CustomerRequest()
		addresses = customer.addresses.add()

		# Asserting that the length of address would be 1
		#assert len(addresses) == 1

		customer.id = round(random.random()*100)
		customer.firstName = input("Enter your first name: ")
		customer.lastName = input("Enter your last name: ")
		customer.email = input("Enter your emaid-id: ")
		customer.phone = input("Enter your phone number: ")
		addresses.flatno = int(input("Enter your flat-no: "))
		addresses.building = input("Enter your building: ")
		addresses.locality = input("Enter your locality: ")
		addresses.city = input("Enter your city: ")
		addresses.country = input("Enter your country: ")
		addresses.isShippingAddress = bool(input("Is this your permanent Shipping Address?: "))
		#customer.addresses.MergeFrom(addresses)
		customer = stub.CreateCustomer(customer)
		
		print (customer)
		print ("----Done----")

	except Exception as e:
		print ("Encountered an exception: {}".format(str(e)))

def get_data(stub, filter):
	print ("Retrieving data . . .")

	try:
		customerdb = customer_pb2.CustomerFilter()

		customerdb.keyword = filter

		data = stub.GetCustomers(customerdb)

		for datum in data:
			print ("The data point queried is : ")

		print ("Data retrieved successfully.")

	except Exception as e:
		print ("Encountered an exception: {}".format(str(e)))

def run():
	channel = grpc.insecure_channel('localhost:50052')
	stub = customer_pb2_grpc.CustomerStub(channel)

	create_customer(stub)

	filter = input("Filter to query the database: ")
	#get_data(stub, filter)

if __name__=="__main__":
	run()