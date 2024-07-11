class mobile:
    contact_list = {}
    def addnew(name, mob):
        mobile.contact_list[name] = mob
    def viewall():
        for name, mob in mobile.contact_list.items():
            print(f'Name = {name}, Mobile = {mob}')
    def search(name):
        l = len(name)
        for n,m in mobile.contact_list.items():
            if n[:l] == name:
                print(f'Name = {n}, Mobile = {m}')

    def delete(name):
        for n in mobile.contact_list:
            if name == n:
               del mobile.contact_list[n]
               print("Contact Removed")
               break
        
    

from mobile import mobile
mobile.addnew('srikanth', 32879)
mobile.addnew('sushanth', 42892)
mobile.addnew('suresh', 43287)


