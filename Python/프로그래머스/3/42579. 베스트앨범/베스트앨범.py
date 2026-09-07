def solution(genres, plays):
    answer = []

    total_by_genre = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        total_by_genre[genre] = total_by_genre.get(genre, 0) + play

    sorted_genres = sorted(total_by_genre.items(), key=lambda x: x[1], reverse=True)

    songs_by_genre = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in songs_by_genre:
            songs_by_genre[genre] = []
        songs_by_genre[genre].append((play, i))

    for genre, _ in sorted_genres:
        songs = songs_by_genre[genre]
        songs.sort(key=lambda x: (-x[0], x[1]))
        top_songs = songs[:2]
        for song in top_songs:
            answer.append(song[1])

    return answer
