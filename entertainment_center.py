import media
import fresh_tometoes

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                             "A marine on an alien planet",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A marine on an alien planet",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=5PSNL1qE6VY")

ratatouille = media.Movie("Ratatouille",
                          "A marine on an alien planet",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                           "A marine on an alien planet",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toy_story, avatar, ratatouille, midnight_in_paris, hunger_games]

fresh_tometoes.open_movies_page(movies)
