class SylogRecord(line: String) {
    var input: String = ""
    var TIMESTAMP: String = ""
    var HOSTNAME: String = ""
    open var APPLICATION_NAME: String = ""
    var PID: Int = 0
    var LOG_ENTRY: String = ""
    val UNDEFINED_PID: Int = -1


    init {
        input = line;
        var auxList: List<String> = input.split(" ")

        // constructing the TIMESTAMP
        TIMESTAMP += (auxList[0] + " ")
        TIMESTAMP += (auxList[1] + " ")
        TIMESTAMP += auxList[2]

        HOSTNAME += auxList[3]

        var APPLICATION_NAME_AUX = auxList[4]
        APPLICATION_NAME = APPLICATION_NAME_AUX.replace("[0-9\\[\\]]".toRegex(), "")
        var STRING_PID = APPLICATION_NAME_AUX.replace("[^0-9]".toRegex(), "")

        if (STRING_PID != "") {
            PID = STRING_PID.toInt()
        } else {
            PID = UNDEFINED_PID
        }

        val listSize = auxList.size
        for (index in 5 until (listSize)) {
            LOG_ENTRY += (auxList[index] + " ")
        }

        LOG_ENTRY = LOG_ENTRY.dropLast(1)
    }

    override fun toString(): String {
        return "%s %s %s[%d]: %s".format(
            this.TIMESTAMP,
            this.HOSTNAME,
            this.APPLICATION_NAME,
            this.PID,
            this.LOG_ENTRY
        )
    }

}