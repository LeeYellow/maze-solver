from django.db import models

class Maze(models.Model):
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    grid = models.JSONField()          # 2D 迷宮格子：0=通路, 1=牆壁
    solution = models.JSONField(null=True, blank=True)  # [(x,y), ...]
    dead_ends = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Maze {self.id} ({self.width}x{self.height})"
