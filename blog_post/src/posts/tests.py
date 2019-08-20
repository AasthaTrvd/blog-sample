from django.test import TestCase
from posts.models import PostModel

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        PostModel.objects.create(title='Post1', content='Post1 Content')
        PostModel.objects.create(title='Post2', content='Post2 Content')
    
    def test_post_title(self):
        """ Verify Post titles """
        post1 = PostModel.objects.get(title='Post1')
        post2 = PostModel.objects.get(title='Post2')

        self.assertEqual(post1.title, 'Post1')
        self.assertEqual(post2.title, 'Post2')

    def test_post_content(self):
        """ Verify Post content """
        post1 = PostModel.objects.get(title='Post1')
        post2 = PostModel.objects.get(title='Post2')
    
        self.assertEqual(post1.content, 'Post1 Content')
        self.assertEqual(post2.content, 'Post2 Content')
