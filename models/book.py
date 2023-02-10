class Book():

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre 


   


# {% endblock %}

# <div>
#     <table>
#       <thead>
#         <tr>
          
#           <th>Title</th>
#           <th>Author</th>
#           <th>Genre</th>
#         </tr>
#       </thead>
#       <tbody>
#         {% for book in book_list %}
#         <tr>
          
#           <td>{{ book.title }}</td>
#           <td>{{ book.author }}</td>
#           <td>{{ boook.genre }}</td>
#         </tr>
#         {% endfor %}
#       </tbody>
#     </table>
#   </div>