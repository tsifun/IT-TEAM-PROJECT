from django.test import TestCase

#testing authentication 

class Tests(TestCase):
    def test_user_profile_model(self):
        # Create a user
        user, user_profile = test_utils.create_user()

        # Check there is only the saved user and its profile in the database
        all_users = User.objects.all()
        self.assertEquals(len(all_users), 1)

        all_profiles = UserProfile.objects.all()
        self.assertEquals(len(all_profiles), 1)

        # Check profile fields were saved correctly
        all_profiles[0].user = user
        all_profiles[0].website = user_profile.website

class Tests(TestCase):

   
    def test_registration_form_is_displayed_correctly(self):
        #Access registration page
        try:
            response = self.client.get(reverse('register'))
        except:
            try:
                response = self.client.get(reverse('rango:register'))
            except:
                return False

        # Check if form is rendered correctly
        # self.assertIn('<h1>Register with Rango</h1>', response.content)
        self.assertIn('<strong>register here!</strong><br />'.lower(), response.content.lower())

        # Check form in response context is instance of UserForm
        self.assertTrue(isinstance(response.context['user_form'], UserForm))

        # Check form in response context is instance of UserProfileForm
        self.assertTrue(isinstance(response.context['profile_form'], UserProfileForm))

        user_form = UserForm()
        profile_form = UserProfileForm()

        # Check form is displayed correctly
        self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())
        self.assertEquals(response.context['profile_form'].as_p(), profile_form.as_p())

        # Check submit button
        self.assertIn('type="submit" name="submit" value="Register"', response.content)

   
    def test_login_form_is_displayed_correctly(self):
        #Access login page
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('rango:login'))
            except:
                return False

        #Check form display
        #Header
        self.assertIn('<h1>Login to Rango</h1>'.lower(), response.content.lower())

        #Username label and input text
        self.assertIn('Username:', response.content)
        self.assertIn('input type="text" name="username" value="" size="50"', response.content)

        #Password label and input text
        self.assertIn('Password:', response.content)
        self.assertIn('input type="password" name="password" value="" size="50"', response.content)

        #Submit button
        self.assertIn('input type="submit" value="submit"', response.content)

    
    def test_login_form_is_displayed_correctly(self):
        #Access login page
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('rango:login'))
            except:
                return False

        #Check form display
        #Header
        self.assertIn('<h1>Login to Rango</h1>'.lower(), response.content.lower())

        #Username label and input text
        self.assertIn('Username:', response.content)
        self.assertIn('input type="text" name="username" value="" size="50"', response.content)

        #Password label and input text
        self.assertIn('Password:', response.content)
        self.assertIn('input type="password" name="password" value="" size="50"', response.content)

        #Submit button
        self.assertIn('input type="submit" value="submit"', response.content)

    def test_login_provides_error_message(self):
        # Access login page
        try:
            response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        except:
            try:
                response = self.client.post(reverse('rango:login'), {'username': 'wronguser', 'password': 'wrongpass'})
            except:
                return False

        print response.content
        try:
            self.assertIn('wronguser', response.content)
        except:
            self.assertIn('Invalid login details supplied.', response.content)

    
	
    def test_login_redirects_to_index(self):
        # Create a user
        test_utils.create_user()

        # Access login page via POST with user data
        try:
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'test1234'})
        except:
            try:
                response = self.client.post(reverse('rango:login'), {'username': 'testuser', 'password': 'test1234'})
            except:
                return False

        # Check it redirects to index
        self.assertRedirects(response, reverse('index'))

   
    def test_upload_image(self):
        # Create fake user and image to upload to register user
        image = SimpleUploadedFile("testuser.jpg", "file_content", content_type="image/jpeg")
        try:
            response = self.client.post(reverse('register'),
                             {'username': 'testuser', 'password':'test1234',
                              'email':'testuser@testuser.com',
                              'website':'http://www.testuser.com',
                              'picture':image } )
        except:
            try:
                response = self.client.post(reverse('rango:register'),
                                 {'username': 'testuser', 'password':'test1234',
                                  'email':'testuser@testuser.com',
                                  'website':'http://www.testuser.com',
                                  'picture':image } )
            except:
                return False

        # Check user was successfully registered
        self.assertIn('thank you for registering!'.lower(), response.content.lower())
        user = User.objects.get(username='testuser')
        user_profile = UserProfile.objects.get(user=user)
        path_to_image = './media/profile_images/testuser.jpg'

        # Check file was saved properly
        self.assertTrue(os.path.isfile(path_to_image))

        
		def test_create_a_new_category(self):
        con = Continents(name="Python")
        con.save()

		
        # Check category is in database
        categories_in_database = Category.objects.all()
        self.assertEquals(len(categories_in_database), 1)
        only_poll_in_database = categories_in_database[0]
        self.assertEquals(only_poll_in_database, cat)

    def test_create_pages_for_categories(self):
        con = Continents(name="Python")
        con.save()

        # create 2 pages for category python
        python_page = Page()
        python_page.category = con
        python_page.title="Localspotpic"
        python_page.url="r'^africa/$', views.africa"
		python_page.url="r'^america/$', views.america"
		python_page.url="r'^europe/$', views.europe"
		python_page.url="r'^asia/$', views.asia"
		python_page.url="r'^australia/$', views.australia"
        python_page.save()

        
        # Check if they both were saved
        python_pages = con.page_set.all()
        self.assertEquals(python_pages.count(), 2)

        #Check if they were saved properly
        first_page = python_pages[0]
        self.assertEquals(first_page, python_page)
        self.assertEquals(first_page.title , "Official Python Tutorial")
        self.assertEquals(first_page.url, "http://docs.python.org/2/tutorial/")

    def test_population_script_changes(self):
        #Populate database
        populate_rango.populate()

        # Check if the category has correct number of views and likes
        con = Continents.objects.get(name='Python')
        self.assertEquals(con.dislikes, 44)
        self.assertEquals(con.likes, 195)

        # Check if the category has correct number of views and likes
        con = Continenets.objects.get(name='Django')
        self.assertEquals(con.dislike, 44)
        self.assertEquals(con.likes, 195)

        # Check if the category has correct number of views and likes
        con = Continents.objects.get(name='Other Frameworks')
        self.assertEquals(con.views, 44)
        self.assertEquals(con.likes, 195)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		