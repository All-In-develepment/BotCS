using Application.Core;
using Application.Tips;
using Domain;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace API.Controllers
{
    [AllowAnonymous]
    public class TipsController : BaseApiController
    {
        [HttpGet]
        public async Task<IActionResult> GetTips([FromQuery] PagingParams param)
        {
            return HandlePagedResult(await Mediator.Send(new ListTips.Query { Params = param }));
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetTip(int id)
        {
            return HandleResult(await Mediator.Send(new Details.Query { Id = id }));
        }

        [HttpPost]
        public async Task<IActionResult> CreateTip(Tip tip)
        {
            return HandleResult(await Mediator.Send(new CreateTip.Command { Tip = tip }));
        }

        [HttpGet("match/{matchId}")]
        public async Task<IActionResult> GetTipByMatchId(string matchId)
        {
            return HandleResult(await Mediator.Send(new FindByMatchId.Query { MatchId = matchId }));
        }

        [HttpGet("status")]
        public async Task<IActionResult> GetTipsWithStatusTrue([FromQuery] PagingParams param)
        {
            return HandlePagedResult(await Mediator.Send(new ListTipWithStatusTrue.Query { Params = param }));
        }

        [HttpPut("{matchid}")]
        public async Task<IActionResult> EditTip(string matchid, Tip tip)
        {
            tip.TipMatchId = matchid;
            return HandleResult(await Mediator.Send(new EditTip.Command { Tip = tip }));
        }
    }
}