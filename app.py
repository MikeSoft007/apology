from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Apology API live and ready!"


# Define the apology endpoint
@get("/apology")
async def apology_endpoint() -> dict:
    # Create the apology message
    apology_message = {
        "message": "I sincerely apologize for using thumbs down emojis instead of unmuting myself to express my opinion during the meeting. It was unprofessional, and I understand that clear and direct communication is essential for effective collaboration. I will ensure to communicate verbally in future discussions. Thank you for understanding."
    }
    #Serialized to JSON
    return apology_message

# Create the LiteStar application
app = Litestar(route_handlers=[apology_endpoint])
