from django.shortcuts import render
from .models import Floor

# Create your views here.


class FloorView:
    def __init__(self, request):
        self.request = request
    def get(self):
        floors = Floor.objects.all()
        return render(self.request, 'listfloor.html', {'floors': floors})


def listFloor(request):
    floors = Floor.objects.all()
    return render(request, 'listfloor.html', {'floors': floors})

        
# def create_view(request):
#     form = FloorForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/floor')
#     context = {'form': form}
#     return render(request, 'create.html', context)



# def update_view(request, id):
#     floor = get_object_or_404(Floor, id=id)
#     form = FloorForm(request.POST or None, instance=floor)
#     if form.is_valid():
#         form.save()
#         return redirect('/floor')
#     context = {'form': form}
#     return render(request, 'create.html', context)

# def delete_view(request, id):
#     floor = get_object_or_404(Floor, id=id)
#     if request.method == 'POST':
#         floor.delete()
#         return redirect('/floor')
#     context = {'floor': floor}
#     return render(request, 'delete.html', context)


# def detail_view(request, id):
#     floor = get_object_or_404(Floor, id=id)
#     context = {'floor': floor}
#     return render(request, 'detail.html', context)
