This microservice does two things:

    allows main program to retrieve backlog of entries
    allows main program to add new entry to backlog

To View Backlog:

    have main program write "view_backlog" to storage_pipeline.txt
    Make program sit and read storage_pipeline.txt until it says "ready_backlog"
    make program write "send_backlog" onto storage_pipeline.txt
    have program wait until "send_backlog" is overwritten
    when "send_backlog" is overwritten, storage_pipeline.txt will contain the backlog
    it will be formatted as follows: [NUMBER OF ENTRIES] // this will be an integer ***** // "*****" divides each entry text // one word per line text etc. ***** text ***** ... ***** end_backlog // signifies end of transmission
    program will be immediately ready for new commands

To add entry:

    have main program write "add_entry" to storage_pipeline.txt
    Make program sit and read storage_pipeline.txt until it says "send_entry"
    make program write the new entry followed by "end_file" onto storage_pipeline.txt
    have program wait until "received_entry" is read
    microservice will then be ready for new commands
