import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyzh85nqc4")
print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg,jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)
avatar.show_trailer()


