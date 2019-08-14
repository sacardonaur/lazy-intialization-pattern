public class LazyCustomer {
  private List<Order> orders;
  private String name;

  public LazyCustomer() {
    this.name = "Juan";
  }

  public List<Order> getOrders() {

    if (this.orders == null){
      this.orders = LoadOrders();
    }

    return orders;
  }
}

public class NotLazyCustomer {
  private List<Order> orders;
  private String name;

  public Customer() {
    this.name = "Juan";
    this.orders = LoadOrders();
  }

  public List<Order> getOrders() {
    return orders;
  }
}
