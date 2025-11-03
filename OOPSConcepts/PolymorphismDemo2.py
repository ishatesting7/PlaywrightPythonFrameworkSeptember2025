class DemoPoly:
    def order_details(self, *args):
        if len(args) == 1:
            return f"Order details for order id: {args[0]}"
        elif len(args) == 2:
            return f"Order details for order id: {args[0]} and product id: {args[1]}"
        else:
            return "Invalid number of arguments"
        
demo = DemoPoly()
demo.order_details(101)
demo.order_details(101, 202)
demo.order_details(101, 202, 303)

class demoPoly2:
    def demo2(self, *args, **kwargs):
        if args and 'action' in kwargs:
            return f"Arguments: {args}, Action: {kwargs['action']}"
        elif args:
            return f"Arguments: {args}"
        elif 'action' in kwargs:
            return f"Action: {kwargs['action']}"
        else:
            return "No arguments or action provided"
demo2 = demoPoly2()
demo2.demo2(1, 2, 3, action="test")
demo2.demo2(1, 2, 3)
demo2.demo2(action="sample")
demo2.demo2()