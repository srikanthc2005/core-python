class customer:
    alist = {}
    def register(self, first_name, last_name, mobile, email, addresses):
        if first_name.isalpha() and last_name.isalpha():
            self.fname = first_name
            self.lname = last_name
            
        self.mobile = mobile
        
        if '@' in email:
            self.email = email

        for atype, address in addresses:
            if atype.lower() in ['home' , 'work' , 'other']:
               self.alist[atype] = address
        print('Information Saved')

    def view_addresses(self):
        for at, add in self.alist.items():
            print(f'{at}  -  {add}')
    def del_address(self, atype):
        if atype in self.alist:
            del self.alist[atype]
            print("Address Deleted")
    def change_mob(self, newmob):
        customer.mobile = newmob
        print('Mobile Changed')

customer = customer()
print()
customer.register('srikanth', 'c', 9490441976, 'cs@gmail.com', [('home', 'Moula Ali'), ('work', 'Suchitra')])
print()
customer.view_addresses()
print()
customer.del_address('home')
customer.view_addresses()
print()
customer.change_mob(9090909090)


