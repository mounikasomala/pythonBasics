class card:
    def __init__(self,imageURL,price,rating,description,deliveryWithin,comments,brandName):
        self.imageURL = imageURL
        self.price = price
        self.rating = rating
        self.description = description
        self.deliveryWithin = deliveryWithin
        self.comments = comments
        self.brandName = brandName
    
    def printBasicDetails(self):
        print("product brand is:",self.brandName)
        print("product price is:",self.price)
        print("product rating is:",self.rating)
        print("product comments is:",self.comments)

commentsForLaptop =["this is good","okay","not bad"]
laptop=card("dummy-url-1",99999,4.5,"exicelent","4 days","good","lenova")

laptop.printAllDetails()

commentsForMobile =["battery is draining","got damaged product","not good"]
mobile=card("dummy-url-2",19999,3.1,"battery is draining","6-days","not good","MI")

mobile.printAllDetails()

commentsForWatch=["very good","good","okay"]
smartWatch=card("dummu-url-2",3999,4.2,"working good","3-days","very good","boat")

smartWatch.printAllDetails()

