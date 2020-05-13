# IMPORTS


class Book:

    def __init__(self):
        super().__init__()
        # SET BOOK SPECIFIC VARIABLES

    def gb_query(self):
        # QUERIES GOOGLE BOOKS IF NECESSARY
        return

    def db_insert(self):
        # INSERTS GB_QUERY INTO DATABASE
        return

    def book_check(self):
        # CHECKS IF BOOK IS IN XML
        # CHECKS IF BOOK IS IN GOOGLE BOOKS
        return

    def get_description(self):
        # BASED ON BOOK_CHECK FUNCTION, GET DESCRIPTION
        # BE AWARE OF EXCEPTION OF RETURNING NO DESCRIPTION 
        # self.description = description
        # IF THIS DOES NOT WORK, LOOK AT TEXT SNIPPET
        return

    def collaborative_recommendations(self, top_n=10):
        # LOAD MODEL/MATRIX HERE
        # IF BOOK IS IN XML DATA,
        # LOOK UP BOOK ON COMPARISON MATRIX
        # RETURN TOP "N" NEARESTNEIGHBORS RECOMMENDATIONS
        # REFERENCE routes/recommendations.py
        return

    def content_recommendations(self, top_n=10):
        # USE get_description FUNCTION OR self.description
        # LOAD THE MODEL/MATRIX HERE
        # MAKE PREDICTIONS
        # RETURN TOP "N" NEARESTNEIGHBORS RECOMMENDATIONS
        # REFERENCE recs.py deleted
        return

    def hybrid_recommendations(self):
        # WEIGHT COLLABORATIVE / CONTENT RECOMMENDATIONS
        return