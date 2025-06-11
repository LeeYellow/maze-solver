from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Max
from .models import Maze
from .utils import generate_maze

def new_maze(request):
    data = generate_maze(61, 41)  # 61x41 大小
    m = Maze.objects.create(
        width=data["width"],
        height=data["height"],
        grid=data["grid"],
        solution=data["solution"],
        dead_ends=data["dead_ends"]
    )
    max_id = Maze.objects.aggregate(Max('id'))['id__max']
    return render(request, "maze_detail.html", {
        "maze_id": m.pk,
        "max_id": max_id or 1,
        "show_solution": False,  # 不顯示解答
    })

def maze_detail(request, pk):
    max_id = Maze.objects.aggregate(Max('id'))['id__max']
    return render(request, "maze_detail.html", {
        "maze_id": pk,
        "max_id": max_id or 1,
        "show_solution": True,
    })

def maze_api(request, pk):
    m = get_object_or_404(Maze, pk=pk)
    return JsonResponse({
        "width": m.width,
        "height": m.height,
        "grid": m.grid,
        "solution": m.solution,
        "dead_ends": m.dead_ends
    })