$(function(){

    console.log("Charts Load Test")

    $('#subject-select').on('change', function (e) {

        $('#type-select').val("current")

    })

    $('#type-select').on('change', function (e) {

        console.log("Type Change")

    })

    DisplayPlayerCountCurrent()

})
