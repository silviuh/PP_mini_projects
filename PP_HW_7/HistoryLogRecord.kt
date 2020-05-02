class HistoryLogRecord(timeStamp: Long, command: String) : Comparable<HistoryLogRecord> {
    var timeStamp: Long = 0
    var command: String = ""

    init {
        this.timeStamp = timeStamp
        this.command = command
    }

    override fun compareTo(other: HistoryLogRecord): Int {
        if (this.timeStamp < other.timeStamp) {
            return -1
        } else if (this.timeStamp > other.timeStamp)
            return 1
        else{
            if (this.command < other.command)
                return -1;
            else if (this.command > other.command)
                return 1
            else return 0;
        }
    }

    override fun toString(): String {
        return "%s".format(this.command)
    }

}