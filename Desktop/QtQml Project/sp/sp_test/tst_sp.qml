import QtQuick 2.0
import QtTest 1.0

TestCase {
    name: "sp"

    function test_case1() {
        compare(1 + 1, 2, "sanity check");
        verify(true);
    }
}
