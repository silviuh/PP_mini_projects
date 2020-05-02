import java.io.File

fun readFileAsLinesUsingReadLines(fileName: String): List<String> = File(fileName).readLines()


fun main() {

    val filePath = "syslog"
    var logEntries: List<String> = readFileAsLinesUsingReadLines(filePath)
    var sysRecords = mutableListOf<SylogRecord>()
    var applicationEntries = mutableMapOf<String, MutableList<SylogRecord>?>()

    for (log in logEntries) {
        var currentRecord = SylogRecord(log)
        sysRecords.add(currentRecord)

        if (applicationEntries.get(currentRecord.APPLICATION_NAME) == null) {
            applicationEntries.put(
                currentRecord.APPLICATION_NAME,
                mutableListOf<SylogRecord>()
            )
        }

        applicationEntries[currentRecord.APPLICATION_NAME]!!.add(currentRecord)
    }

    for ((key, value) in applicationEntries) {
        applicationEntries[key]!!.sortBy { it.LOG_ENTRY }
    }

    val filteredEntries = mutableListOf<List<SylogRecord>>()
    for ((key, value) in applicationEntries) {
        filteredEntries
            .add(applicationEntries[key]
            !!.filter { it.PID != -1 })
    }

    for (AppList in filteredEntries) {
        for (entry in AppList) {
            File("filtered_entries").appendText(entry.toString() + "\n")
        }
    }


}