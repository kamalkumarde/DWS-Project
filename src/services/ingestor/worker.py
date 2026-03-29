class IngestionWorker:
    def __init__(self, source, processor, sink, dlq):
        self.source = source
        self.processor = processor
        self.sink = sink
        self.dlq = dlq

    def run(self):
        self.source.connect()
        def on_message(raw_data):
            event, error = self.processor.process(raw_data)
            if event:
                self.sink.write(event)
            else:
                self.dlq.bury(raw_data)
        self.source.start_streaming(on_message)