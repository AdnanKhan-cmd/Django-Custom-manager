from django.db import models
import json
import os

# Create your models here.
class JsonHandler(models.Manager):
    def raw_list_data(self):
        input_file = open('movies.json', 'r')
        raw_data = json.load(input_file)
        list_objects = []
        for p_data in raw_data:
            movie_obj = self.model(
                pk=p_data["id"],
                name=p_data["name"],
                image=p_data["imgPath"],
                duration=p_data["duration"],
                )
            movie_obj.userRating = p_data["userRating"]
            list_objects.append(movie_obj)
        return list_objects
    
    def raw_details(self, pk):
        input_file = open('movies.json', 'r')
        raw_data = json.load(input_file)
        list_objects = []
        for p_data in raw_data:
            if int(p_data["id"]) == pk:
                movie_obj = self.model(
                    name = p_data["name"],
                    image=p_data["imgPath"],
                    language = p_data["language"],
                    duration = p_data["duration"],
                    description = p_data["description"],
                )
                movie_obj.sub_heading = "(" + p_data["mpaaRating"]["type"] + ": " + p_data["mpaaRating"]["label"] + ")"
                movie_obj.genre_list =  ", ".join(p_data["genre"])
                movie_obj.userRating = p_data["userRating"]
                return movie_obj
        return []
        
    def ajax_name(self, q):
        input_file = open('movies.json', 'r')
        raw_data = json.load(input_file)
        list_objects = []
        for p_data in raw_data:
            if q.lower() in (p_data["name"]).lower():
                movie_obj = self.model(
                pk=p_data["id"],
                name=p_data["name"],
                image=p_data["imgPath"],
                duration=p_data["duration"],
                )
                movie_obj.userRating = p_data["userRating"]
                list_objects.append(movie_obj)
        return list_objects
            



class Genre(models.Model):
    name = models.CharField(max_length=30)


class Rating(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    ratinng = models.FloatField()
    image = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    us_rating = models.CharField(max_length=4)
    language = models.CharField(max_length=15)

    objects = JsonHandler()
