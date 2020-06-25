import unittest
import pyperclip
from contact import Contact

class TestContact(unittest,TestCase):
    def setUp(self):
        self.new_contact = contact("Morin","Memzo","0704603872","mchepkemoi435@gmail.com")
    def tearDown(self):
        Contact.contact_list = [] 
        def test_init(self):
            self.assertEqual(self.new_contact.first_name,"Morin")
            self.assertEqual(self.new_contact.last_name,"Memzo")
            self.assertEqual(self.new_contact.phone_number,"0704603872")
            self.assertEqual(self.new_contact.email,"mchepkemoi435@gmail.com")

        def test_save_contact(self):
            self.new_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),1) 

        def test_save_multiple_contact(self):
            self.new_contact.save_contact()
            test_contact = Contact("Test","User","0728868073","test@user.com")
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)      
        def test_delete_contact(self):
            self.new_contact.save_contact()
            test_contact = Contact("Test","User","0728868073","test@user.com")
            test_contact.save_contact()

            self.new_contact.delete_contact()
            self.assertEqual(len(Contact.contact_list),1)

        def delete_contact(self):
            Contact.contact_list.remove(self)

        def test_find_contact_by_number(self):
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0728868073","test@user.com")
            test_contact.save_contact()

            found_contact = Contact.find_by_number("0728868073")
            self.assertEqual(found_contact.email,test-contact.email)


        def test_contact_exists(self):
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0728868073","test@user.com")
            test_contact.save_contact()

            contact_exists = Contact.contact_exist("0728868073")

            self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)
     
    def test_copy_email(self):
        self.new_contact.save_contact()
        Contact.copy_email("0728868073")

        self.assertEqual(self.new_contact.email,pyperclip.paste())

            if _name_ == '_main_':
                unittest.main()