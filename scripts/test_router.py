from app.rag.router import QuestionRouter

router = QuestionRouter()

while True:

    question = input("\nQuestion : ")

    result = router.route(question)

    print(result)