package cz.lipovcan.buybread;

/**
 * This class was automatically generated by the data modeler tool.
 */

@javax.persistence.Entity
public class Order implements java.io.Serializable {

	static final long serialVersionUID = 1L;

	@javax.persistence.GeneratedValue(generator = "ORDER_ID_GENERATOR", strategy = javax.persistence.GenerationType.AUTO)
	@javax.persistence.Id
	@javax.persistence.SequenceGenerator(sequenceName = "ORDER_ID_SEQ", name = "ORDER_ID_GENERATOR")
	private java.lang.Long id;

	@javax.persistence.ManyToOne(cascade = {javax.persistence.CascadeType.ALL}, fetch = javax.persistence.FetchType.EAGER)
	private cz.lipovcan.buybread.Product product;

	private int amount;

	private float price;

	private java.lang.Boolean is_payed;

	private java.lang.String first_name;

	private java.lang.String last_name;

	private java.lang.String address;

	private int phone_number;

	public Order() {
	}

	public java.lang.Long getId() {
		return this.id;
	}

	public void setId(java.lang.Long id) {
		this.id = id;
	}

	public cz.lipovcan.buybread.Product getProduct() {
		return this.product;
	}

	public void setProduct(cz.lipovcan.buybread.Product product) {
		this.product = product;
	}

	public int getAmount() {
		return this.amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public float getPrice() {
		return this.price;
	}

	public void setPrice(float price) {
		this.price = price;
	}

	public java.lang.Boolean getIs_payed() {
		return this.is_payed;
	}

	public void setIs_payed(java.lang.Boolean is_payed) {
		this.is_payed = is_payed;
	}

	public java.lang.String getFirst_name() {
		return this.first_name;
	}

	public void setFirst_name(java.lang.String first_name) {
		this.first_name = first_name;
	}

	public java.lang.String getLast_name() {
		return this.last_name;
	}

	public void setLast_name(java.lang.String last_name) {
		this.last_name = last_name;
	}

	public java.lang.String getAddress() {
		return this.address;
	}

	public void setAddress(java.lang.String address) {
		this.address = address;
	}

	public int getPhone_number() {
		return this.phone_number;
	}

	public void setPhone_number(int phone_number) {
		this.phone_number = phone_number;
	}

	public Order(java.lang.Long id, cz.lipovcan.buybread.Product product,
			int amount, float price, java.lang.Boolean is_payed,
			java.lang.String first_name, java.lang.String last_name,
			java.lang.String address, int phone_number) {
		this.id = id;
		this.product = product;
		this.amount = amount;
		this.price = price;
		this.is_payed = is_payed;
		this.first_name = first_name;
		this.last_name = last_name;
		this.address = address;
		this.phone_number = phone_number;
	}

}