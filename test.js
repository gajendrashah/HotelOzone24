function rms_calc() {

    var checkbox_r = $("#check1").val();
    var rm_dis = $("#id_room_discount").val()
    var room_amount = $("#idss_organization").val();
    var res_cost = $("#id_Resturent_amt").val();
    var res_disc = $("#res_desc").val()
    var advance_amt = $("#advance_amt").val();


    var room_discount = $("#room-discount").val()
    var resturent_discount = $("#resturent_discount").val()
    var rem_blc = $("#rem_blc").val()
    console.log(vat)

    if (rm_dis !== "" && res_cost !== "") {
        var room_disc = parseFloat(room_amount) - parseFloat(rm_dis)
        var res_desc = parseFloat(res_cost) - parseFloat(res_disc)
        var after_disc = room_disc + res_desc
        console.log(after_disc)
    }
    if (checkbox_r === "true") {
        $("#vat_count").val(after_disc * 13 / 100)
        var vat = $("#vat_count").val()
        var payable_amt = ((parseFloat(room_discount) + parseFloat(vat) + parseFloat(resturent_discount) + parseFloat(rem_blc) - parseFloat(advance_amt)))

        $("#ids_total_amt").val(payable_amt)
        var amount_paid = payable_amt - parseFloat($("#last_value").val())
        $("#amount_paid").val(amount_paid)


    }
    else {
        $("#vat_count").val(0)
        var vat = $("#vat_count").val()
        var payable_amt = ((parseFloat(room_discount) + parseFloat(resturent_discount) + parseFloat(rem_blc) - parseFloat(advance_amt)))

        $("#ids_total_amt").val(payable_amt)
        var amount_paid = payable_amt - parseFloat($("#last_value").val())
        $("#amount_paid").val(amount_paid)


    }
    var inner_data = `  
<div class="row" id ="get_data" >
<div class="col-md-6 py-1">
    <label for="advance_amt" class="py-1 h6">Room Discount:</label>
</div>
<div class="col-md-6 py-1">
    <input type="text" class="form-control"  value = "${room_disc}" id="room-discount" name="room-discount"
        placeholder="" readonly="">

</div>

<div class="col-md-6 py-1">
    <label for="resturent_discount" class="py-1 h6">Resturenr Discount:</label>
</div>
<div class="col-md-6 py-1">
    <input type="text" class="form-control" value = "${res_desc}" id="resturent_discount" name="resturent_discount"
        placeholder="" readonly="">

</div>
</div>

`

    output += $("#calc-details").html(inner_data)
   

}