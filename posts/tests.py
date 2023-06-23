from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


#tests fr my mode;s
class PostModelTests(TestCase):
    #create a test model database with the post 'this is just a test
    def setUp(self):
        Post.objects.create(text='this is just a test')
    #testing if the content matches the post at database 
    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{post.text}'
        self.assertEqual(expected_object_name,'this is just a test')  

"""
 creatng a test fr the HomePage
 does it actually exist and return a HTTP 200 response?
 does it use HomePageView as the view?
 does it use home.html as the template
 """  

class HomePageViewTest(TestCase):
    def setUp(self):
      Post.objects.create(text='this is just another test') 

    def test_view_url_exist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)  

    def test_view_by_url_name(self):
        resp = self.client.get(reverse('home')) 
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')




