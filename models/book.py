class Book():

    def __init__(self, title, author, genre, description, in_stock):
        self.title = title
        self.author = author
        self.genre = genre 
        self.description = description 
        self.in_stock = in_stock

    def __nonzero__(self):
        return self.in_stock !=0 

   


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