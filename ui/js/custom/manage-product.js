var productModal = $("#productModal");
$(function () {
  //JSON data by API call
  $.get(productListApiUrl, function (response) {
    if (response) {
      var table = "";
      $.each(response, function (index, product) {
        table +=
          '<tr data-id="' +
          product.product_id +
          '" data-name="' +
          product.name +
          '" data-unit="' +
          product.unit_id +
          '" data-price="' +
          product.price_per_unit +
          '">' +
          "<td>" +
          product.name +
          "</td>" +
          "<td>" +
          product.unit_name +
          "</td>" +
          "<td>" +
          product.price_per_unit +
          "</td>" +
          '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
      });
      $("table").find("tbody").empty().html(table);
    }
  });
});

// Save Product
$("#saveProduct").on("click", function () {
  // If we found id value in form then update product detail
  var data = $("#productForm").serializeArray();
  var requestPayload = {
    name: null,
    unit_id: null,
    price_per_unit: null,
  };
  console.log("data", data);
  for (var i = 0; i < data.length; ++i) {
    var element = data[i];
    switch (element.name) {
      case "name":
        requestPayload.name = element.value;
        break;
      case "uoms":
        requestPayload.unit_id = element.value;
        break;
      case "price":
        requestPayload.price_per_unit = element.value;
        break;
    }
  }
  console.log("data 2222", requestPayload);
  callApi("POST", productSaveApiUrl, {
    data: JSON.stringify(requestPayload),
  });
});

// Delete Product
$(document).on("click", ".delete-product", function () {
  console.log("Delete button clicked"); // Check if this logs when you click the button
  var tr = $(this).closest("tr");
  var data = {
    product_id: tr.data("id"),
  };
  var isDelete = confirm(
    "Are you sure to delete " + tr.data("name") + " item?"
  );
  if (isDelete) {
    console.log("Sending delete request for product ID:", data.product_id);
    callApi("POST", productDeleteApiUrl, data);
  }
});

//Close and open 'Add New Product' modal

productModal.on("hide.bs.modal", function () {
  $("#id").val("0");
  $("#name, #unit, #price").val("");
  productModal.find(".modal-title").text("Add New Product");
});

productModal.on("show.bs.modal", function () {
  //JSON data by API call
  $.get(uomListApiUrl, function (response) {
    if (response) {
      var options = '<option value="">--Select--</option>';
      $.each(response, function (index, uom) {
        options +=
          '<option value="' + uom.unit_id + '">' + uom.unit_name + "</option>";
      });
      $("#uoms").empty().html(options);
    }
  });
});
