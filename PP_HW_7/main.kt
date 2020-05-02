import java.io.File
import java.time.Instant
import java.time.LocalDate
import java.time.ZoneId
import java.time.format.DateTimeFormatter
import javax.swing.ViewportLayout

fun readFileDirectlyAsText(fileName: String): String = File(fileName).readText(Charsets.UTF_8)

fun <T : Comparable<T>> max(first: T, second: T): T {
    val result = first.compareTo(second)
    return if (result <= 0) second else first
}

fun searchAndReplace(
    givenMap: MutableMap<Long, MutableList<HistoryLogRecord>?>,
    historyLogRecordToReplace: HistoryLogRecord,
    historyLogRecordToReplaceWith: HistoryLogRecord
) {
    for ((Key, Value) in givenMap) {
        for (i in 0 until Value!!.size) {
            if (Value!![i] == historyLogRecordToReplace) {
                Value!!.set(i, historyLogRecordToReplaceWith)
            }
        }
    }
}

fun main() {

    val historyLogFilePath = "/home/silviuh/IdeaProjects/PP_LAB_7/src/history.log.1"
    val fileBuffer = readFileDirectlyAsText(historyLogFilePath)

    val StartDates = "(Start-Date: (\\d+)-(\\d+)-(\\d+)\\s+(\\d+):(\\d+):(\\d+))"
        .toRegex()
        .findAll(fileBuffer)
        .toList()
        .map { it.groupValues[1] }
        .toList()

    var CommandLines = "((Commandline): (.*))"
        .toRegex()
        .findAll(fileBuffer)
        .toList()
        .map { it.groupValues[1] }
        .toList()

    var initialMap = mutableMapOf<Long, MutableList<HistoryLogRecord>?>()

    val datesIterator = StartDates.iterator()
    for ((index, dateInstr) in datesIterator.withIndex()) {
        var actualDate = "((\\d+)-(\\d+)-(\\d+))"
            .toRegex()
            .find(dateInstr)!!
            .value
            .split("-")

        var aux = LocalDate.parse(
            actualDate[2] + "-" + actualDate[1] + "-" + actualDate[0],
            DateTimeFormatter.ofPattern("dd-MM-yyyy")
        )

        val unixTimeStamp = aux.atStartOfDay(ZoneId.systemDefault())
            .toInstant()
            .epochSecond

        if (initialMap.get(unixTimeStamp) == null) {
            initialMap.put(
                unixTimeStamp,
                mutableListOf<HistoryLogRecord>()
            )
        }

        initialMap[unixTimeStamp]!!.add(HistoryLogRecord(unixTimeStamp, CommandLines[index]))
    }

    var maxLog: HistoryLogRecord = HistoryLogRecord(0, "")

    for ((Key, Value) in initialMap) {
        for (i in 0 until Value!!.size) {
            maxLog = max(maxLog, Value!![i])
        }
    }

    searchAndReplace(
        initialMap,
        maxLog,
        HistoryLogRecord(0, "")
    )

    var outputFile = File("map_of_log_records")

    for ((key, log) in initialMap) {
        outputFile.appendText(key.toString() + " ---> ")
        for (i in 0 until log!!.size)
            outputFile.appendText(
                (log[i].toString()).replace(
                    "(Commandline: )".toRegex(), ""
                ) + ", "
            )
        outputFile.appendText("\n")
    }

    print(maxLog)
}