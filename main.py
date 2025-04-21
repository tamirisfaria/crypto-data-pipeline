from sqlalchemy.orm import sessionmaker
from database.db import get_engine
from database.models import Base, Cryptocurrency, Price
from services.coincap_api import fetch_cryptos

def main():
    engine = get_engine()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cryptos, prices = fetch_cryptos(limit=20)  # Coleta das 20 principais moedas

    # Inserção ou atualização simples
    for crypto in cryptos:
        existing = session.query(Cryptocurrency).filter_by(id=crypto['id']).first()
        if existing:
            existing.name = crypto['name']
            existing.symbol = crypto['symbol']
            existing.rank = crypto['rank']
        else:
            session.add(Cryptocurrency(**crypto))

    session.commit()

    for price in prices:
        session.add(Price(**price))

    session.commit()
    session.close()
    print("Dados inseridos com sucesso.")

if __name__ == "__main__":
    main()
