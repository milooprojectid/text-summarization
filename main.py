from summarization import Preprocessing
import summarization
from Mnewspaper import getNews

if __name__ == "__main__":
    # print('main')
    
    article = "Kekhawatiran akan menyebarnya virus Corona masih tinggi. Seluruh dunia sekarang siaga demi menahan masuknya virus yang belum ada obatnya itu.Virus yang kabarnya berasal dari sop kelelawar ini mulai menggoyang ekonomi China karena situasi yang tidak stabil. Pagi tadi, pasar saham China pun ambruk sejak pembukaan perdagangan.Hari ini merupakan hari perdana Bursa China jualan setelah libur panjang Imlek. Sayangnya, tak lama setelah pembukaan, Indeks Komposit Shanghai anjlok hingga 9%."
    # print(Preprocessing.fit())

    url = 'https://www.cnnindonesia.com/gaya-hidup/20200224123114-255-477472/vaksin-remdesivir-cikal-bakal-antivirus-corona'

    news = getNews(url)
    summarization.fit(news)