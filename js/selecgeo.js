$('select').change(function(){
    alert($(this).data('id'));
});

<select>
<option data-id="1">one</option>
    <option data-id="2">two</option>
    <option data-id="3">three</option>
    </select>
