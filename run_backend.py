import os
import sys

# Point to backend directory
root_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(root_dir, "backend")

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

os.chdir(backend_dir)

if __name__ == "__main__":
    import uvicorn

    print("===================================================")
    print(" Starting What Did I Miss? - Backend")
    print(" URL: http://127.0.0.1:8000")
    print(" API Docs: http://127.0.0.1:8000/docs")
    print("===================================================\n")

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
