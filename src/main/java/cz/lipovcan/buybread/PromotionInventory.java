package cz.lipovcan.buybread;

/**
 * This class was automatically generated by the data modeler tool.
 */

@javax.persistence.Entity
@javax.xml.bind.annotation.XmlRootElement
public class PromotionInventory implements java.io.Serializable {

	static final long serialVersionUID = 1L;

	private int daysToExpire;

	private int id;

	private java.lang.String name;

	private int amount;

	private int price;

	public PromotionInventory() {
	}

	public int getDaysToExpire() {
		return this.daysToExpire;
	}

	public void setDaysToExpire(int daysToExpire) {
		this.daysToExpire = daysToExpire;
	}

	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public java.lang.String getName() {
		return this.name;
	}

	public void setName(java.lang.String name) {
		this.name = name;
	}

	public int getAmount() {
		return this.amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public int getPrice() {
		return this.price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public PromotionInventory(int daysToExpire, int id, java.lang.String name,
			int amount, int price) {
		this.daysToExpire = daysToExpire;
		this.id = id;
		this.name = name;
		this.amount = amount;
		this.price = price;
	}

}