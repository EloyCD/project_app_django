from django.http import HttpResponse
from .db_utils import connect_db, create_record

def create_game(request):
    conn = connect_db()
    data = {
        'name': 'New Game',
        'genre': 'Puzzle',
        # ... otros campos
    }
    create_record(conn, 'game_table', data)
    conn.close()
    return HttpResponse("Game created successfully")






    


