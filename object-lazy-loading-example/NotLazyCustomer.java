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
