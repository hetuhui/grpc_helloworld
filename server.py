from concurrent import futures
import time
import grpc
import customer_pb2
import customer_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Customers(customer_pb2.CustomerServicer):
	def CreateCustomer(self, request, context):
		print ("The recieved message was {}".format(request))

		return customer_pb2.CustomerResponse(id = request.id,
											 success = True)

	def GetCustomers(self, request, context):
		print ("The recieved message for PartI was {}".format(request))

		searchstr = request.keyword

		print ("The keyword is {}".format(searchstr))

#		if (searchstr == )
		#customer_pb2.CustomerRequest()


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	customer_pb2.add_CustomerServicer_to_server(Customers(), server)

	server.add_insecure_port('[::]:50052')
	server.start()

	print ("-------------------The Server has started-------------------------")
	try:
	    while True:
	        time.sleep(_ONE_DAY_IN_SECONDS)
	        print ("-------------------The Server will continue-------------------------")
	except KeyboardInterrupt:
	    server.stop(0)
	    print ("-------------------The Server has stopped-------------------------")


if __name__ == '__main__':
    serve()