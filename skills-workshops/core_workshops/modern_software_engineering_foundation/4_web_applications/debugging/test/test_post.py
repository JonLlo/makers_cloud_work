import pytest
from ..lib.post import Post

class TestPost:
    def test_post_initialization(self):
        post = Post("Test Title", "Test Content", ["tag1", "tag2"])
        assert post.title == "Test Title"
        assert post.content == "Test Content"
        assert post.tags == ["tag1", "tag2"]

    def test_post_with_default_tags(self):
        post = Post("Title", "Content")
        assert post.tags == []

    def test_post_attributes_are_accessible(self):
        post = Post("Title", "Content", ["tag"])
        post.title = "New Title"
        post.content = "New Content"
        post.tags = ["new_tag"]
        assert post.title == "New Title"
        assert post.content == "New Content"
        assert post.tags == ["new_tag"]
