$(function(){

    console.log("COMPARE LOAD TEST")

    let numbers = []

    $("#test-button").click(function(){
        numbers.push($("#test-number").val())
        let player = player_count_past_24_hours_compare(numbers)

        console.log(player)

    })

})
