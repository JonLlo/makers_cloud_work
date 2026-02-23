import pytest
from ..lib.post_repository import PostRepository
from ..lib.post import Post

class TestPostRepository:
    @pytest.fixture
    def post_repository(self, db_connection):
        return PostRepository(db_connection)

    def test_create_and_find_post(self, post_repository, db_connection):
        db_connection.seed("seeds/posts.sql")
        post = Post("Title", "Content", ["tag"])
        post_repository.create(post)
        posts = post_repository.all()
        assert len(posts) == 6
        assert posts[5].title == "Title"
        assert posts[5].content == "Content"
        assert posts[5].tags == ["tag"]

    def test_find_post_by_id(self, post_repository, db_connection):
        db_connection.seed("seeds/posts.sql")
        post = Post("Test Title", "Test Content", ["test"])
        post_repository.create(post)
        
        posts = post_repository.all()
        found_post = post_repository.find(posts[5].id)
        
        assert found_post.title == "Test Title"
        assert found_post.content == "Test Content"
        assert found_post.tags == ["test"]

    def test_delete_post(self, post_repository, db_connection):
        db_connection.seed("seeds/posts.sql")
        post = Post("Title to Delete", "Content", ["tag"])
        post_repository.create(post)
        
        posts = post_repository.all()
        post_id = posts[0].id
        
        post_repository.delete(post_id)
        
        remaining_posts = post_repository.all()
        assert len(remaining_posts) == 5
