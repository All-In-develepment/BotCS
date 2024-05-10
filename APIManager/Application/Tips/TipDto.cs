namespace Application.Tips
{
    public class TipDto
    {
        public int TipId { get; set; }
        public string TipMatchId { get; set; }
        public DateTime TipDate { get; set; }
        public string TeamA { get; set; }
        public string TeamB { get; set; }
        public string FavoriteTeam { get; set; }
        public List<string> TipMaps { get; set; }
        public List<string> TipMapOdd { get; set; }
        public string TipMessageId { get; set; }
        public List<string> TipsMapResult { get; set; }
        public bool TipStatus { get; set; }
    }
}