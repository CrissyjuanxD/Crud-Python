class Client {
  #dni
  constructor(first_name = "Consumidor", last_name = "Final", dni = "9999999999") {
    // Método constructor para inicializar los atributos de la clase Cliente
    this.first_name = first_name;
    this.last_name = last_name;
    this.#dni = dni; // Atributo privado para almacenar el número de identificación del cliente
  }

  get dni() {
    // Getter para obtener el valor del atributo privado _dni
    return this.#dni;
  }

  set dni(value) {
    // Setter para asignar un nuevo valor al número de identificación del cliente, con validación de longitud
    if (value.length === 10 || value.length === 13) {
      this.#dni = value;
    } else {
      this.#dni = "9999999999"; // Retorna el valor predeterminado si la longitud no es válida
    }
  }

  toString() {
    // Método especial para representar la clase Cliente como una cadena
    return `Cliente: ${this.first_name} ${this.last_name}`;
  }

  show() {
    // Método para imprimir los detalles del cliente en la consola
    console.log('   Nombres    Dni');
    console.log(`${this.first_name} ${this.last_name}  ${this.dni}`);
  }
}

class RetailClient extends Client {
  constructor(first_name = "Cliente", last_name = "Final", dni = "9999999999", card = false) {
    // Método constructor para inicializar los atributos de la clase RetailClient
    super(first_name, last_name, dni); // Llama al constructor de la clase padre
    this._discount = card ? 10 : 0; // Descuento del cliente minorista
  }

  get discount() {
    // Getter para obtener el valor del descuento del cliente minorista
    return this._discount;
  }

  toString() {
    // Método especial para representar la clase RetailClient como una cadena
    return `Cliente Minorista: DNI:${this.dni} Nombre:${this.first_name} ${this.last_name} Descuento:${this.discount}`;
  }

  show() {
    // Método para imprimir los detalles del cliente minorista en la consola
    console.log(`Cliente Minorista: DNI:${this.dni} Nombre:${this.first_name} ${this.last_name} Descuento:${this.discount}`);
  }
}

class VipClient extends Client {
  constructor(first_name = "Consumidor", last_name = "Final", dni = "9999999999") {
    // Método constructor para inicializar los atributos de la clase VipClient
    super(first_name, last_name, dni); // Llama al constructor de la clase padre
    this._limit = 10000; // Límite de crédito del cliente VIP
  }

  get limit() {
    // Getter para obtener el valor del límite de crédito del cliente VIP
    return this._limit;
  }

  set limit(value) {
    // Setter para asignar un nuevo valor al límite de crédito del cliente VIP, con validación de rango
    this._limit = (value < 10000 || value > 20000) ? 10000 : value;
  }

  toString() {
    // Método especial para representar la clase VipClient como una cadena
    return `Cliente Vip: DNI:${this.dni} Nombre:${this.first_name} ${this.last_name} Cupo:${this.limit}`;
  }

  show() {
    // Método para imprimir los detalles del cliente VIP en la consola
    console.log(`Cliente Vip: DNI:${this.dni} Nombre:${this.first_name} ${this.last_name} Cupo:${this.limit}`);
  }
}

if (require.main === module) {
  let retail_cli1 = new RetailClient();
  let retail_cli2 = new RetailClient("Daniel", "Vera", "0914122419", true);
  let vip_cli1 = new VipClient("Erick", "Vera", "0914122412");
  let vip_cli2 = new VipClient("Yadira", "Bohorquez", "0914122411");
  vip_cli2.limit = 15000;
  let clients = [retail_cli1, retail_cli2, vip_cli1, vip_cli2];
  clients.forEach(cli => console.log(cli));
  clients.forEach(cli => cli.show());
}
