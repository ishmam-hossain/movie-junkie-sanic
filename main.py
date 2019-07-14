from apps import app
import multiprocessing


if __name__ == "__main__":
    workers = multiprocessing.cpu_count()
    app.run(host="0.0.0.0", workers=workers, port=8888, debug=True)
