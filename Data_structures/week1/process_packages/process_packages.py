# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.pos = 1
    def process(self, request):
        # write your code here
        if self.finish_time:
            if self.finish_time[-1] <= request.arrived_at:
                was_dropped, started_at = False, request.arrived_at
                time = request.arrived_at + request.time_to_process
                self.finish_time.append(time)
            else:
                self.pos += 1
                if self.pos <= self.size:
                    was_dropped, started_at = False, self.finish_time[-1]
                    time = request.arrived_at + request.time_to_process
                    self.finish_time.append(time)
                else:
                    was_dropped, started_at = True, -1
        else:
            was_dropped, started_at = False, request.arrived_at
            time = request.arrived_at + request.time_to_process
            self.finish_time.append(time)
        return Response(was_dropped, started_at)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
